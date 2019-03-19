
function lint {
    docker build -f test.Dockerfile -t hasherator_test . &&
    docker run --rm hasherator_test flake8 .
}

function run {
    python3 -u -m src.main "$@"
}

function test {
    docker build -f test.Dockerfile -t hasherator_test . &&
    docker run --rm hasherator_test
}

case $1 in
    lint)
        lint
        ;;
    run)
        run "${@:2}"
        ;;
    test)
        test
        ;;
    *)
        echo "Please specify an option"
        echo "\tlint\tRun a linter against source and tests"
        echo "\trun\tRun the hasherator - remember to provide CSV files as arguments"
        echo "\ttest\tRun unit tests"
        exit 1
        ;;
esac
