/* Toggles railroad diagram <-> BNF text for the topic whose header was clicked. */
function switchBnf(el) {
  var sib = el.nextElementSibling, rail = null, bnf = null;
  while (sib && sib.tagName !== "H2" && sib.tagName !== "H3") {
    if (sib.getAttribute) {
      if (sib.getAttribute("name") === "railroad") rail = sib;
      if (sib.tagName === "PRE" && sib.getAttribute("name") === "bnf") bnf = sib;
    }
    sib = sib.nextElementSibling;
  }
  if (!rail || !bnf) return;
  var showBnf = rail.style.display !== "none";
  rail.style.display = showBnf ? "none" : "";
  bnf.style.display = showBnf ? "block" : "none";
}
