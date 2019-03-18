
function lint {
    docker build -f test.Dockerfile -t hasherator_test . &&
    docker run --rm hasherator_test flake8 .
}

function test {
    docker build -f test.Dockerfile -t hasherator_test . &&
    docker run --rm hasherator_test
}

case $1 in
    lint)
        lint
        ;;
    test)
        test
        ;;
    *)
        echo "Please specify an option"
        echo "\tlint\tRun a linter against source and tests"
        echo "\ttest\tRun unit tests"
        exit 1
        ;;
esac
