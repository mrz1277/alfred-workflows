all: clean 4shared

clean:
	rm -f workflows/*.alfredworkflow

4shared:
	cd net.yakiyama.alfred.4shared ; \
	zip ../workflows/4shared.alfredworkflow . -r --exclude=*.DS_Store* --exclude=*.pyc*