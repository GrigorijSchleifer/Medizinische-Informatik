-- Absätze, die mit "Merksatz" beginnen, in ein <div class="merksatz"> packen
-- (Aussehen: style.css). Die .qmd-Dateien bleiben unverändert.
function Para(el)
  local first = el.content[1]
  if first and first.t == "Str" and first.text:match("^Merksatz") then
    return pandoc.Div({ el }, pandoc.Attr("", { "merksatz" }))
  end
end
