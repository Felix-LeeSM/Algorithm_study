defmodule Solution do
  @spec compressed_string(word :: String.t()) :: String.t()
  def compressed_string(word) do
    word
    |> String.graphemes()
    |> case do
      [] ->
        []

      [first | rest] ->
        Enum.reduce(rest, {first, 1, []}, fn
          char, {char, cnt, acc} ->
            {char, cnt + 1, acc}

          char, {prev_char, cnt, acc} ->
            {char, 1, [{prev_char, cnt} | acc]}
        end)
    end
    |> then(fn {char, cnt, acc} -> [{char, cnt} | acc] end)
    |> do_cut()
    |> Enum.reverse()
    |> stringify()
  end

  def do_cut(acc), do: do_cut(acc, [])

  def do_cut([], acc), do: acc

  def do_cut([{char, num} | t], [[{char, _} | _] = hd | rest]) when num > 9,
    do: do_cut([{char, num - 9} | t], [[{char, 9} | hd] | rest])

  def do_cut([{char, num} | t], [[{char, _} | _] = hd | rest]),
    do: do_cut(t, [[{char, num} | hd] | rest])

  def do_cut([{char, num} | t], acc) when num > 9,
    do: do_cut([{char, num - 9} | t], [[{char, 9}] | acc])

  def do_cut([{char, num} | t], acc), do: do_cut(t, [[{char, num}] | acc])

  def stringify([]) do
    ""
  end

  def stringify(acc) do
    stringify(acc, [])
  end

  def stringify([[{char, num} | t1] | t2], acc) do
    stringify([t1 | t2], ["#{num}#{char}" | acc])
  end

  def stringify([[] | t2], acc) do
    stringify(t2, acc)
  end

  def stringify([], acc) do
    Enum.join(acc, "")
  end
end
