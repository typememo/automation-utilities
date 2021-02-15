#!/bin/bash

#
# Functions
#
function usage() {
  cat <<EOT
Usage: update-paleo
EOT
  return 0
}

function help() {
  cat <<EOT
Usage:
  update-paleo

Description:
  Update paleo channel blogposts.

Options:
  -h  Show help
EOT
  return 0
}

#
# Option analysis
#
for OPT in "$@"; do
  case $OPT in
  -h)
    help
    exit 0
    ;;
  esac
done

#
# Update paleo channel blogposts
#
export PYTHONPATH=$HOME/typememo/tau/lib/google

CWD=$(
  cd $(dirname $0)
  pwd
)
cd $CWD

python3 -m pip install --upgrade \
  google-api-python-client \
  google-auth-httplib2 \
  google-auth-oauthlib
python3 $CWD/main.py

#
# Git
#
TYPEMEMO="$HOME/typememo"
FILE="$HOME/typememo/blog/content/posts/life/paleo-channel-blogposts/manuscript.md"
HAS_COMMITTED_FILE=$(git add --dry-run ${FILE})

cd ${TYPEMEMO}

if [ ! -z "${HAS_COMMITTED_FILE}" ]; then
  git add ${FILE}
  git commit -m "[#117] Auto update paleo channel blogposts"
  git push
else
  echo "Nothing will be commited file."
fi

#
# End
#
cd -
echo "End of the paleo channel blogposts updater"
