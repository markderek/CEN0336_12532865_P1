# Comando que mostre a pasta/diretório onde você está
printf "\033[0;34mDiretório:	\033[0m\n"	
pwd

# Comando que gere uma lista com detalhes do conteúdo da sua pasta HOME e redirecione essa lista para o arquivo: lista_HOME.txt
printf "\033[0;34mLista detalhada do diretório 'Home':	\033[0m\n"
ls -l ~	
printf "\033[0;34m...Copiando lista detalhada do diretório 'Home' para o arquivo 'lista_HOME.txt'...\033[0m\n"
ls -l ~ > lista_HOME.txt

# Comando que mostre a pasta/diretório onde você está
printf "\033[0;34mData e tempo:	\033[0m\n"
date
