// Compatibilité des WebView anciennes (Android 7 à 10 sans mise à jour de la WebView) :
// complète String.prototype.replaceAll (Chrome 85) et structuredClone (Chrome 98),
// utilisés par l'exécution Svelte. Chargé avant tout autre script ; sans effet sur une WebView à jour.
(function () {
  'use strict';
  if (!String.prototype.replaceAll) {
    Object.defineProperty(String.prototype, 'replaceAll', {
      configurable: true,
      writable: true,
      value: function (motif, remplacement) {
        if (motif instanceof RegExp) {
          if (!motif.global) throw new TypeError('replaceAll exige une expression régulière globale');
          return this.replace(motif, remplacement);
        }
        var cherche = String(motif);
        var echappe = cherche.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
        if (typeof remplacement === 'function') return this.replace(new RegExp(echappe, 'g'), remplacement);
        var r = String(remplacement).replace(/\$/g, '$$$$');
        return this.replace(new RegExp(echappe, 'g'), r);
      }
    });
  }
  if (typeof globalThis.structuredClone !== 'function') {
    var copier = function (v, vus) {
      if (v === null || typeof v !== 'object') return v;
      if (vus.has(v)) return vus.get(v);
      var c;
      if (v instanceof Date) return new Date(v.getTime());
      if (v instanceof RegExp) return new RegExp(v.source, v.flags);
      if (v instanceof Map) { c = new Map(); vus.set(v, c); v.forEach(function (x, k) { c.set(copier(k, vus), copier(x, vus)); }); return c; }
      if (v instanceof Set) { c = new Set(); vus.set(v, c); v.forEach(function (x) { c.add(copier(x, vus)); }); return c; }
      if (ArrayBuffer.isView(v)) return v.slice();
      if (v instanceof ArrayBuffer) return v.slice(0);
      c = Array.isArray(v) ? [] : {};
      vus.set(v, c);
      Object.keys(v).forEach(function (k) { c[k] = copier(v[k], vus); });
      return c;
    };
    globalThis.structuredClone = function (v) { return copier(v, new Map()); };
  }
})();
