defmodule Emobatch.EmotionResponse do
  defstruct [:anger, :joy, :fear, :sadness, :surprise]

  defimpl Poison.Encoder, for: Emobatch.EmotionResponse do
    def encode(%{anger: anger, joy: joy, fear: fear, sadness: sadness, surprise: surprise}, options) do
      Poison.Encoder.BitString.encode("#{joy},#{anger},#{fear},#{sadness},#{surprise}", options)
    end
  end
end

defmodule Emobatch.Parser do
  alias Emobatch.EmotionResponse

  @input "input.csv"
  @output "output.csv"
  @indico_url "https://apiv2.indico.io/emotion/batch"
  @indico_key System.get_env("INDICO_API_KEY")

  @doc """
  Processes all tweets and saves to @output
  """
  def process do
    tweets = chunk_tweets(100)

    File.open(@output, [:read, :write], fn(file) ->
      for t <- tweets do
        process_batch(t, file)
        Process.sleep(1000)
      end
    end)
  end

  @doc """
  Processes one batch of tweets
  """
  def process_batch(batch, file) do
    header = %{"X-ApiKey" => @indico_key}

    tweets = Enum.map(batch, fn([x, _]) -> x end)
    times_utc = Enum.map(batch, fn([_, y]) -> y end)

    {:ok, data} = Poison.encode(%{data: tweets})

    case HTTPoison.post(@indico_url, data, header, hackney: [:insecure]) do
      {:ok, %HTTPoison.Response{body: body}} ->
        {:ok, %{"results" => body}} = Poison.decode(body, as: %{results: [%EmotionResponse{}]})

        Stream.zip(batch, times_utc)
        |> Stream.zip(body)
        |> Stream.map(&join_tweet &1)
        |> Enum.each(fn(result) -> IO.write(file, result) end)

      {:error, _} -> IO.inspect {self(), "ERROR: bad response"}
    end
  end

  @doc """
  Processes tweets into chunks

  Reads file
  |> removes newline
  |> splits into [tweet, time]
  |> chunks by 'chunk'
  """
  def chunk_tweets(chunk) do
    File.stream!(@input)
    |> Stream.map(&String.replace_trailing(&1, "\n", ""))
    |> Stream.map(&String.split(&1, ~r{,(?=\d+$)}))
    |> Enum.chunk(chunk)
  end

  @doc """
  Joins tweet with emotion data
  """
  def join_tweet({{[tweet, time], _}, er}) do
    "'#{tweet}',#{er["joy"]},#{er["anger"]},#{er["fear"]},#{er["sadness"]},#{er["surprise"]},#{time}\n"
  end
end
