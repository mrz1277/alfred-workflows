all: clean 4shared

4shared:
	cd net.yakiyama.alfred.4shared ; \
	zip ../4shared.alfredworkflow . -r --exclude=*.DS_Store* --exclude=*.pyc*

clean:
	rm -f *.alfredworkflow