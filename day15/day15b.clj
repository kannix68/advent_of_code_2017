#!/usr/bin/env clojure

; Advent of code 2017, AoC day 15 pt2.
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

;** test data (as a var(iable))
(def teststr 
"0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5")

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

; solve/assert test-data
(let [
  seqA (iterate gen-A 65)
  seqB (iterate gen-B 8921)
  iters 1056
  fullseqA (take iters (filter #(= 0 (mod %1 4)) seqA))
  fullseqB (take iters (filter #(= 0 (mod %1 8)) seqB))
  result (count (filter true? (map #(=(mod %1 65536) (mod %2 65536)) fullseqA fullseqB)))
  expected 1
  ]
  (println "test-iters" iters)
  ;(println "fullseqA" fullseqA)
  ;(println "fullseqB" fullseqB)
  (assert-msg (= result expected) (str "test-result " result " should be " expected))
)

(let [
  seqA (iterate gen-A 65)
  seqB (iterate gen-B 8921)
  iters 5000000
  fullseqA (take iters (filter #(= 0 (mod %1 4)) seqA))
  fullseqB (take iters (filter #(= 0 (mod %1 8)) seqB))
  result (count (filter true? (map #(=(mod %1 65536) (mod %2 65536)) fullseqA fullseqB)))
  expected 309
  ]
  (println "test-iters" iters)
  ;(println "fullseqA" fullseqA)
  ;(println "fullseqB" fullseqB)
  (assert-msg (= result expected) (str "test-result " result " should be " expected))
)

; solve my specific data input
(let [
  datastr (slurp "day15.in")
  inputs (map #(read-string (re-find #"\d+" %1)) (explode-lines datastr))
  seqA (iterate gen-A (first inputs))
  seqB (iterate gen-B (last inputs))
  iters 5000000
  fullseqA (take iters (filter #(= 0 (mod %1 4)) seqA))
  fullseqB (take iters (filter #(= 0 (mod %1 8)) seqB))
  result (count (filter true? (map #(=(mod %1 65536) (mod %2 65536)) fullseqA fullseqB)))
  ]
  ;(println (map #(re-find #"\d+" (explode-lines datastr))))
  (println "first input=" (first inputs) ", second input=" (last inputs))
  (println "result=" result)
)
