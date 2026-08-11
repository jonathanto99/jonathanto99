MOCK PHARMACEUTICAL ENVIRONMENTAL MONITORING DATASET v1.0

This package is entirely synthetic and is intended only for R/Python/SQL practice, portfolio work, and analytics training.
It is not GMP data, not a validated system, and not a model EM program. Do not use the included limits, sampling design, or analytic assumptions to establish facility controls.

FILES
- mock_pharma_em_dataset_v1_0.xlsx: Excel workbook with all relational tables, data dictionary, and README.
- em_results.csv: Primary viable EM observations, one sample per row.
- personnel_monitoring.csv: Glove/gown contact-plate observations.
- sampling_sites.csv: Site master including method and illustrative limits.
- rooms.csv: Room master.
- facility_events.csv: Fictional context for look-back and investigation exercises.
- data_dictionary.csv: Fields and basic definitions.

EM RESULTS: 180-day period in 2025. Includes active air, settle plates, and contact plates. Covers production suites, RABS, sterility test rooms, development labs, corridors, gown-in/out, personnel and material airlocks.
Embedded practice signals: RABS action excursion on 2025-04-22; HALL-01 elevated period 2025-05-10 through 2025-06-15; GWO-01 upward drift after 2025-04-15; OP-04 personnel-monitoring increase during May.

Suggested R entry point:
em <- read.csv("em_results.csv", stringsAsFactors = FALSE)
sites <- read.csv("sampling_sites.csv", stringsAsFactors = FALSE)
rooms <- read.csv("rooms.csv", stringsAsFactors = FALSE)