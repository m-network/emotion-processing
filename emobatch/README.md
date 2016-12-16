# Emobatch
Batch process twitter tweets for emotion using Indico API.

# Requirements
Elixir v1.3.4

Erlang 19

# Getting started
`Emobatch.Parser.process` takes `input.csv` and processes each line and saves the results to `output.csv`.

```
$ mix deps.get
$ export INDICO_API_KEY=<your api key>
$ iex -S mix

iex(1)> Emobatch.Parser.process
...
```
