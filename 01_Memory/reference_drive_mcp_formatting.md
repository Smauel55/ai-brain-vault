---
name: reference_drive_mcp_formatting
description: "Google Drive MCP can't make a formatted native Doc; use HTML upload to get highlight into Google Docs"
metadata: 
  node_type: memory
  type: reference
  originSessionId: aeced60e-3f8b-4c7d-9854-cbf61fe8df5a
---

How to deliver a FORMATTED document to Samuel's Google Drive via the Google Drive MCP (`create_file`), learned 2026-06-06 building Caught Up AI opener test docs. (The Drive MCP itself has been connected and working since 2026-05-08: list/search/read/create/copy/download/metadata/permissions — no delete.)

- `create_file` only auto-converts `text/plain` -> native Google Doc (and `text/csv` -> Sheet). A native Doc made this way is PLAIN: no background-color highlight, no rich formatting.
- HTML does NOT auto-convert: uploading `contentMimeType: text/html` (even with the deprecated `mimeType` target set) stays an `.html` file. But an `.html` file in Drive opens in Google Docs ("Open with Google Docs" / File > Save as Google Docs) with formatting preserved, including `<span style="background-color:#FFF3A0">` -> yellow highlight. This is the way to get highlight into Google Docs through this connector.
- Binary `.docx`/`.rtf` is impractical: it must be passed as `base64Content`, and a real docx is ~55k base64 chars. Reproducing that verbatim is unreliable and corrupts the file. Avoid.
- For TEXT content (plain, html, rtf) authored directly in `textContent`, fidelity is reliable. Verify by comparing the returned `fileSize` to the local source byte count (exact match = clean upload).
- No delete/trash tool exists in this connector (only create, copy, download, read_file_content, get_file_metadata, search_files). Test files must be deleted by hand.
- Practical recipe used: a Python renderer emits one minimal HTML file per doc (native h1/h2/h3, inline style only on highlight spans + labels), Read it, pass as `textContent` with `contentMimeType: text/html`, drop into a folder via `parentId`.

Related: [[reference_vault_infrastructure]], [[project_caught_up_ai]].
