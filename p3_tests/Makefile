TESTFILES := $(wildcard *.jeff)
TESTS := $(TESTFILES:.jeff=.test)

.PHONY: all

all: gen_expecteds $(TESTS)

nogen: $(TESTS) #call this if you want to test without repulling the expected files from oracle

gen_expecteds:
	@rm -f $*.err *.unparse.expected
	@python3 run.py

%.test:
	@rm -f $*.unparse $*.err $*.json
	@touch $*.unparse
	@echo "TEST $*"
	@../jeffc $*.jeff -u $*.unparse 2> $*.err ;\
	PROG_EXIT_CODE=$$?;\
	if [ $$PROG_EXIT_CODE != 0 ]; then \
		echo "jeffc error:"; \
		cat $*.err; \
		exit 1; \
	fi; \
	diff -B --ignore-all-space $*.unparse $*.unparse.expected; \
	STDOUT_DIFF_EXIT=$$?;\
	exit $$STDOUT_DIFF_EXIT || echo "Tests passed"

clean: #Removes all generated files (i.e. not the .jeff files"
	rm -f *.unparse *.err *.json *.expected
