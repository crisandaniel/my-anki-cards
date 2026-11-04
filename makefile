.PHONY: fa af

ANKIOPS_COLLECTION_ROOT := $(CURDIR)
export ANKIOPS_COLLECTION_ROOT

$(info Collection root: ${ANKIOPS_COLLECTION_ROOT})

fa:
	ankiops files-to-anki

af: 
	ankiops anki-to-files
