
function test {
    docker build -f test.Dockerfile -t hasherator_test . &&
    docker run --rm hasherator_test
}

case $1 in
    test)
        test
        ;;
    *)
        echo "Please specify an option"
        echo "\ttest\tRun unit tests"
        exit 1
        ;;
esac
