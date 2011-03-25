SCRIPT=$(readlink -f ${PWD}/${BASH_SOURCE})
TOP_PATH=`dirname $SCRIPT`
TOP_PATH="$TOP_PATH/.."
export mg="$TOP_PATH/env/bin/python $TOP_PATH/lbforum_site/manage.py"
