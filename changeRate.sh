git log --format=format: --name-only | egrep -v '^$' | sort \ | uniq -c | sort -r | head -5
