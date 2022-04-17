package main

import (
	"github.com/gorilla/mux"
	"log"
	"net/http"
)

func main() {
	//http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
	//	w.Write([]byte("Hello World!"))
	//})
	rtr := mux.NewRouter()
	rtr.HandleFunc("/{topic}", func(w http.ResponseWriter, r *http.Request) {
		vars := mux.Vars(r)
		w.Write([]byte("Topic: " + vars["topic"]))
	})
	http.Handle("/", rtr)

	err := http.ListenAndServe(":3000", nil)
	if err != nil {
		log.Fatal(err)
	}
}
