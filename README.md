# MoodleCensusTableAlloc

## Setup

```zsh
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade pandas
```

## Data

The following files are excluded in `.gitignore` but necessary for correct functioning of the script:

`tutor_list.csv` &mdash;

- A list of tutors to be excluded from the allocation.

	```
	tutor_zID
	z3141592
	z6535897
	z9323846
	```

	_(if there are no tutors in the class roll, just leave this empty after the first line)_
	<br />
	<br />

`moodle.csv` &mdash;

- The "Participants" class roll from Moodle.

	```
	Username,"First name",Surname,"Email address", [...]
	z2643383,Alice,Bob,alice.bob@example.com, [...]
	z2795028,Charlie,Dennis,charlie.dennis@example.com, [...]
	z8419712,Evelyn,Farnsworth,evelyn.farnsworth@example.com, [...]
	```