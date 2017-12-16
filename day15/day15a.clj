#!/usr/bin/env clojure

; Advent of code 2017, AoC day 15 pt1.
; This solution by kannix68, @ 2017-12-15.
; tested on clojure 1.9

(require '[clojure.string :as str]) ; clj str ops

(defn assert-msg [condit msg]
  "check condition, fail with message on false, print message otherwise"
  (if (not condit)
    (assert condit (str "assert-ERROR:" msg))
    (println "assert-OK:" msg))
)

;** problem solution

; LIB
(defn explode-lines [str]
  "explode a (multiline) string into list-of-lines,
   by splitting on newlines"
  (str/split str #"\r?\n")
)

; PROB
(defn gen-next [fact, n]
  "generator compute function"
  (mod (* fact n) 2147483647)
)

(defn gen-A [n]
  "generator A"
  (gen-next 16807 n)
)

(defn gen-B [n]
  "generator B"
  (gen-next 48271 n)
)


;** MAIN

;(println (gen-A (gen-A 65)))
;(println (gen-B 8921))

(comment
;(take 5 (repeatedly #(rand-int 11)))
(println
  (take 5 (iterate gen-A 65))
)
(println
  (take 5 (iterate gen-B 8921))
)
)

; solve/assert test-data
(let [
  seqA (iterate gen-A 65)
  seqB (iterate gen-B 8921)
  iters 5
  result (count (filter true? (map #(=(mod %1 65536) (mod %2 65536)) (take iters seqA) (take iters seqB))))
  expected 1
  ]
  ;(println "test-string\n" teststr)
  ;(println "transposed list-of-lists") (println loltr)
  (assert-msg (= result expected) (str "test-result " result " should be " expected))
)

; solve my specific data input
(let [
  datastr (slurp "day15.in")
  inputs (map #(read-string (re-find #"\d+" %1)) (explode-lines datastr))
  seqA (iterate gen-A (first inputs))
  seqB (iterate gen-B (last inputs))
  iters 40000000 ;40000000
  result (count (filter true? (map #(=(mod %1 65536) (mod %2 65536)) (take iters seqA) (take iters seqB))))
  ]
  ;(println (map #(re-find #"\d+" (explode-lines datastr))))
  (println "first input=" (first inputs) ", second input=" (last inputs))
  (println "result=" result)
)
