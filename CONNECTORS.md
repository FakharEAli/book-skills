# Connectors

Book Skills workflows are tool-agnostic. Each step names a **category**; at runtime Claude looks for any connected tool whose name matches that category and uses it. If none is connected, it uses the fallback and says so. Nothing breaks when a tool is missing.

| Category | Used for | Detect tools whose names contain | Fallback |
|---|---|---|---|
| **Call recorder** | debriefs, VOC mining, post-mortems | `fathom`, `gong`, `fireflies`, `granola`, `zoom` + `transcript` / `meeting` | ask the user to paste the transcript or notes |
| **Email** | drafting outreach, follow-ups, reply review | `gmail`, `outlook`, `create_draft`, `search_threads` | write drafts to `assets/sequences/` |
| **Calendar** | prep before upcoming calls, booking advances | `calendar`, `list_events`, `suggest_time` | ask for the call time |
| **Prospecting / enrichment** | building and scoring lists, trigger events | `clay`, `apollo`, `common-room`, `search-companies`, `search-contacts`, `prospect` | `web-research` skill / web search + a CSV the user provides |
| **Web research** | company research, review mining, competitor pages | `web-research` skill, `exa`, `scrapling`, `WebFetch`, `WebSearch` | ask for URLs or pasted text |
| **Docs** | prep sheets, proposals, offer sheets | `notion`, Claude Docs, `google-drive`, `docs` | markdown files in `assets/` |
| **Decks** | proposals, magnet PDFs | `gamma`, `canva`, `pptx` skill | markdown outline |
| **Forms** | scorecard / quiz lead magnets | `typeform`, `forms` (create unpublished; publishing is a send-type action) | markdown form spec + scoring logic |
| **Database** | pipeline tables, magnet responses (optional) | `supabase`, `airtable`, `execute_sql` | the workspace markdown files (default) |
| **LinkedIn** | connection notes, DMs, posts | none officially; browser tools only if the user asks | copy-paste drafts; the user reports sends and replies manually |
| **Chat** | weekly pipeline digest | `slack`, `teams` | print in the conversation |

**Defaults:** the workspace markdown files are the system of record. External tools are optional outputs, never the only copy.

**Safety:** reading from connected tools is fine. Anything that sends, posts, publishes, books or shares (email send, Slack post, calendar invite, form publish, deck share) is drafted first and done only after the user says yes. The plugin's outbound-guard hook enforces a confirmation prompt on send-type tools.
