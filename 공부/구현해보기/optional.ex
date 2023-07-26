defmodule Optional do
  defstruct value: nil, reason: nil

  def of({:ok, value}), do: %Optional{value: value}
  def of({:error, reason}), do: %Optional{value: nil, reason: reason}
  def of(%Optional{} = optional), do: optional
  def of(value), do: %Optional{value: value}

  def or_else(%Optional{value: nil}, func) when is_function(func, 0), do: func.() |> of()
  def or_else(%Optional{value: nil}, value), do: value |> of()
  def or_else(%Optional{} = optional, _), do: optional

  def is_present?(%Optional{value: nil}), do: false
  def is_present?(%Optional{}), do: true

  def is_nil?(%Optional{value: nil}), do: true
  def is_nil?(%Optional{}), do: false

  def if_present(%Optional{value: nil}, func) when is_function(func, 0), do: nil

  def if_present(%Optional{value: _}, func) when is_function(func, 0),
    do: (func.() && nil) || nil

  def if_present(%Optional{value: nil}, func) when is_function(func, 1), do: nil

  def if_present(%Optional{value: value}, func) when is_function(func, 1),
    do: (func.(value) && nil) || nil

  def filter(%Optional{value: nil} = optional, func) when is_function(func, 1), do: optional

  def filter(%Optional{value: value} = optional, func) when is_function(func, 1),
    do: if(func.(value), do: optional, else: %Optional{})

  def map(%Optional{value: nil} = optional, func) when is_function(func, 1), do: optional

  def map(%Optional{value: value}, func) when is_function(func, 1),
    do: func.(value) |> of()

  def get!(%Optional{value: nil, reason: reason}) when not is_nil(reason), do: raise(reason)
  def get!(%Optional{value: value}) when not is_nil(value), do: value

  def get(%Optional{value: value}), do: value

  def get(%Optional{value: nil}, func) when is_function(func, 0), do: func.()
  def get(%Optional{value: nil}, value), do: value
  def get(%Optional{value: value}, _), do: value

  def get_result(%Optional{value: nil, reason: nil}), do: {:error, :empty_optional}
  def get_result(%Optional{value: nil, reason: reason}), do: {:error, reason}
  def get_result(%Optional{value: value}), do: {:ok, value}

  def get_result(%Optional{value: nil}, func) when is_function(func, 0), do: {:ok, func.()}
  def get_result(%Optional{value: nil}, value), do: {:ok, value}
  def get_result(%Optional{value: value}, _), do: {:ok, value}
end
