-- Bekannte Abkürzungen aus abkuerzungen.tsv beim Überfahren mit der Maus erklären:
-- jedes Kürzel im Fließtext wird zu <span class="abk" title="…"> (Aussehen: style.css).
-- Überschriften, Links und das Abkürzungsverzeichnis selbst bleiben unverändert,
-- die .qmd-Dateien sowieso.

local dir = PANDOC_SCRIPT_FILE and pandoc.path.directory(PANDOC_SCRIPT_FILE) or "."
local tips = {}     -- Kürzel -> Tooltip-Text
local byfirst = {}  -- erstes Zeichen -> Kürzel, längste zuerst

local header = true
for line in io.lines(pandoc.path.join({ dir, "abkuerzungen.tsv" })) do
  if header then
    header = false
  else
    local key, long, meaning = line:gsub("\r$", ""):match("^([^\t]*)\t([^\t]*)\t?(.*)$")
    if key and key ~= "" then
      local tip = meaning ~= "" and (long .. " — " .. meaning) or long
      -- "AU / eAU" = zwei Kürzel; "SNOMED CT" -> erstes Wort (Pandoc trennt an Leerzeichen)
      for variant in (key .. " / "):gmatch("(.-) / ") do
        local word = variant:match("^(%S+)")
        if word and not tips[word] then
          tips[word] = tip
          local c = word:sub(1, 1)
          byfirst[c] = byfirst[c] or {}
          table.insert(byfirst[c], word)
        end
      end
    end
  end
end
for _, list in pairs(byfirst) do
  table.sort(list, function(a, b) return #a > #b end)
end

-- Buchstabe/Ziffer oder Umlaut-Byte (>= 128) = Teil eines Wortes; "-" und Satzzeichen nicht
local function isword(c)
  return c ~= "" and (c:match("%w") ~= nil or c:byte() >= 128)
end

-- Text eines Wortes in Str/Span-Stücke zerlegen; nil, wenn kein Kürzel darin steckt
local function split(text)
  local out, last, i, n = {}, 1, 1, #text
  while i <= n do
    local hit
    if i == 1 or not isword(text:sub(i - 1, i - 1)) then
      for _, k in ipairs(byfirst[text:sub(i, i)] or {}) do
        if text:sub(i, i + #k - 1) == k and not isword(text:sub(i + #k, i + #k)) then
          hit = k
          break
        end
      end
    end
    if hit then
      if i > last then table.insert(out, pandoc.Str(text:sub(last, i - 1))) end
      table.insert(out, pandoc.Span(pandoc.Str(hit), pandoc.Attr("", { "abk" }, { title = tips[hit] })))
      i = i + #hit
      last = i
    else
      i = i + 1
    end
  end
  if last == 1 then return nil end
  if last <= n then table.insert(out, pandoc.Str(text:sub(last))) end
  return out
end

function Pandoc(doc)
  local input = quarto and quarto.doc and quarto.doc.input_file or ""
  if input:match("anhang%-abkuerzungen") then return nil end
  return doc:walk({
    traverse = "topdown",
    Header = function(el) return el, false end,
    Link = function(el) return el, false end,
    Span = function(el)
      if el.attributes.title then return el, false end  -- schon von Hand erklärt
    end,
    Str = function(el)
      local parts = split(el.text)
      if parts then return parts, false end
    end,
  })
end
