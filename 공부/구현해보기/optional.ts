export class Optional<T> {
  private static throwEmptyError(): never {
    throw new Error('value is not defined');
  }
  public static of<S>(value: S): Optional<S> {
    if (value === undefined || value === null) Optional.throwEmptyError();
    return new Optional<S>(value);
  }
  public static ofNullable<S>(value?: S): Optional<S> {
    return new Optional<S>(value);
  }

  public static empty<S>(): Optional<S> {
    return new Optional<S>();
  }

  private constructor(private readonly value?: T) {}

  public get(): T {
    if (this.value === undefined || this.value === null) Optional.throwEmptyError();
    return this.value;
  }

  public orElse(other: T): T {
    if (this.value === undefined || this.value === null) return other;
    return this.value;
  }

  public orElseGet(fn: () => T): T {
    if (this.value === undefined || this.value === null) return fn();
    return this.value;
  }

  public map<S>(fn: (value: T) => S): Optional<S> {
    if (this.value === undefined || this.value === null) return Optional.empty<S>();
    return Optional.of(fn(this.value));
  }

  public filter(fn: (value: T) => boolean): Optional<T> {
    if (this.value === undefined || this.value === null || !fn(this.value)) return Optional.empty<T>();
    return Optional.empty<T>();
  }

  public isPresent() {
    return this.value !== undefined && this.value !== null;
  }

  public ifPresent(fn: () => void) {
    if (this.value !== undefined && this.value !== null) fn();
  }

  public ifPresentOrElse(fn: () => void, elseFn: () => void) {
    this.value !== undefined && this.value !== null ? fn() : elseFn();
  }

  public ifAbsent(fn: () => void) {
    if (this.value === undefined || this.value === null) fn();
  }

  public orElseThrow(fn: Error | (() => never)) {
    if (this.value === undefined || this.value === null) {
      if (fn instanceof Error) throw fn;
      fn();
    }
  }
}
