
function build {
    local_setup
    pyinstaller --onefile src/main.py
}

function lint {
    docker build -f test.Dockerfile -t hasherator_test . &&
    docker run --rm hasherator_test flake8 .
}

function local_setup {
    python3 -m venv venv &&
    . venv/bin/activate &&
    python3 -m pip install --upgrade pip &&
    pip3 install -r requirements/test.txt &&
    pip3 install -r requirements/build.txt
}

function run {
    python3 -u -m src.main "$@"
}

function test {
    docker build -f test.Dockerfile -t hasherator_test . &&
    docker run --rm hasherator_test
}

case $1 in
    build)
        build
        ;;
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
