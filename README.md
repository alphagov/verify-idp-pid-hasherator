# verify-idp-pid-hasherator

Standalone app to hash event PIDs in the same way the event emitter does.

## Running the Hasher

The control script's `run` argument can be passed a number of CSV files to hash PIDs in.
The script will parse the headers in the CSV and interactively prompt you to choose the PID column, and either a column for the IDP ID or to supply it directly.
For example:

```
./ha.sh run path/to/csv1.csv path/to/csv2.csv ...
```

## Tests

### Unit Tests

To run the unit tests, run

```
./ha.sh test
```

This builds a docker image with the test source and uses pytest to execute the tests themselves.
