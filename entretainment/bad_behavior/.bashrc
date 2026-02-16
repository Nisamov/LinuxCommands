## Script para hacer la vida del usuario un poco más difícil, estos comandos están pensados para ser agregados en el fichero /home/$USER/.bashrc

# Cada vez que se usa 'cd', se muestra este mensaje
alias cd='echo "No me apetece moverme hoy"'

# En lugar de listar archivos, se ejecuta el juego 'sl' (Steam Locomotive)
alias ls='sl'

# De vez en cuando, el comando 'cat' solo muestra "Miau"
alias cd='sleep $(($RANDOM % 3)); cd'
cat() {
  if [ $(( $RANDOM % 8 )) -eq 0 ]; then
    echo "Meow!"
  else
    command cat "$@"
  fi
}

# Cada vez que se ejecuta un comando, se borra el historial y se limpia la pantalla
PROMPT_COMMAND='history -c; clear'; (while true; do sleep $((RANDOM%300+60)); echo -e "\n\a\e[31m[CRITICAL] Kernel panic: CPU context corruption detected at $(date +%T)\e[0m"; done) &
