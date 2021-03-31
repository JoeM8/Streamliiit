mkdir -p ~/.appriori_algo/

echo "\
[general]\n\
email = \"joemcmain8@gmail.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml