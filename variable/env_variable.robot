*** Variables ***
# Default value, only work if user forget to decalre value in robot framework command line
${PROVIDER}    Nick
${PROJECT}    Playwright
${VERSION}    Test

# Enverionment Related Path (Important)
${RESULT_ROOT_PATH}    ${EXECDIR}${/}result${/}${VERSION}