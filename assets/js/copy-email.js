/*
 * Click-to-copy email address.
 *
 * Progressive enhancement: the element stays a real `mailto:` link, so
 * middle-click, "Copy link address", and browsers without the async
 * Clipboard API (or on a non-secure origin) all keep working normally.
 * Kept out of main.min.js so no npm build step is required.
 */
(function () {
  'use strict';

  function flash(el) {
    var label = el.querySelector('.copy-email__label');
    if (!label || el.classList.contains('is-copied')) return;

    var original = label.textContent;
    el.classList.add('is-copied');
    label.textContent = 'Copied!';

    window.setTimeout(function () {
      el.classList.remove('is-copied');
      label.textContent = original;
    }, 1600);
  }

  document.addEventListener('click', function (event) {
    var link = event.target.closest ? event.target.closest('.copy-email') : null;
    if (!link) return;

    var address = link.dataset.email;
    if (!address || !navigator.clipboard) return; // let the mailto: proceed

    event.preventDefault();
    navigator.clipboard.writeText(address).then(
      function () {
        flash(link);
      },
      function () {
        window.location.href = link.href; // copy refused — fall back to mailto:
      }
    );
  });
})();
