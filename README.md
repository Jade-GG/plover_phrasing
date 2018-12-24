# plover phrasing
This is my phrasing system for plover, using python dictionaries.

This system is based on frequency data gathered from datamuse and also from experience.

The basic premise of this is writing sentences like "I didn't know that" or "you don't really care about" in one stroke, by defining starting left bank stroke words, middle vowel words, and ending words.

Here's a quick overview:  
**Starting words**  
- `SWR`: `I`
- `KPWR`: `you`
- `KWHR`: `he`
- `SKWHR`: `she`
- `TWH`: `they`
- `TWR`: `we`
- `TKWH`: `it`

**Middle words**  
- `OE`: `don't` (`AOE` makes `really don't`, `OEU` makes `don't really`)
- `AU`: `didn't` (`AOU` makes `really didn't`, `AEU` makes `didn't really`)
- `E`: `doesn't` (`AE` makes `really doesn't`, `EU` makes `doesn't really`)
- `O`: `can't` (`AO` makes `really can't`, `OU` makes `can't really`)
- `A` or `U`: `really`
- `AOEU`: `don't even`

**Ending words** (non-exhaustive)  
- `PB`: `know`
- `P`: `want`
- `RPL`: `remember`
- `BL`: `believe`
- `FG`: `forget`
- `R`: `are`, or `am`, or `is` depending on starting word
- et cetera

I will also soon merge this with a similar system that uses the same ending words.
