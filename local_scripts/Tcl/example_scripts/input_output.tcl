# Esritura de fichero.txt
set fileId [open "fichero.txt" "w"]
puts $fileId "Contenido fichero"
close $fileId