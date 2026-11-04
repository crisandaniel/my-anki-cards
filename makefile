.PHONY: fa af

ANKIOPS_COLLECTION_ROOT := $(CURDIR)
export ANKIOPS_COLLECTION_ROOT

$(info Collection root: ${ANKIOPS_COLLECTION_ROOT})

.ankiops.db:
	ankiops init

fa: .ankiops.db
	ankiops files-to-anki

af: .ankiops.db
	ankiops anki-to-files
