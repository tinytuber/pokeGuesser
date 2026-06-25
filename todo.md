# Pokemon Grid Game — TODO

## Phase 1: Build Your Data
- [x] Finalize spreadsheet schema (columns for id, name, types, evolution, legs, HMs, height, weight)
- [x] Create CSV and fill in all 151 Pokemon
- [x] Make judgment calls on edge cases (legless Pokemon, dual colors, etc.)
- [x] Write Python script to convert CSV → SQLite database
- [x] Manually run test queries to verify data looks correct

## Phase 2: Define Categories
- [ ] Write a Python file defining all categories (label + SQL condition per category)
- [ ] Include categories for: each type, evolution stage, does not evolve, single vs dual type, legs, each HM, height threshold, weight threshold
- [ ] Write a validation function: given two categories, query DB and return matching Pokemon
- [ ] Test every category pair to confirm no combination returns 0 results

## Phase 3: Grid Generation
- [ ] Write a function to randomly pick 3 row + 3 column categories (no repeats)
- [ ] For each of the 9 cells, run the validation query
- [ ] If any cell returns 0 results, discard and regenerate
- [ ] Return the valid grid (6 category labels + valid Pokemon per cell)

## Phase 4: Backend (Flask)
- [ ] Set up a basic Flask project structure
- [ ] Build endpoint: GET /grid → generates and returns a grid
- [ ] Build endpoint: POST /guess → receives Pokemon name + cell position, returns valid/invalid
- [ ] Test both endpoints with curl or Postman before touching the frontend

## Phase 5: Frontend
- [ ] Build static 3x3 grid in HTML/CSS (hardcoded first, no logic)
- [ ] Add autocomplete search input that filters 151 Pokemon names as user types
- [ ] Wire autocomplete so selecting a Pokemon assigns it to the active cell
- [ ] On submission, call /guess endpoint and mark cell correct or incorrect
- [ ] On page load, call /grid endpoint and render the real categories

## Phase 6: Polish
- [ ] Prevent re-guessing an already solved cell
- [ ] Show number of valid Pokemon per cell after it's solved
- [ ] Add a "New Game" button that regenerates the grid
- [ ] General styling pass

## Phase 7: Deploy
- [ ] Push project to GitHub
- [ ] Choose hosting platform
- [ ] Configure app for production environment
- [ ] Deploy and test live
