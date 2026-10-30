# TypeScript patterns

Short examples for the rules in `SKILL.md`.

## Tagged unions

```ts
// Contradictory states are possible:
type Upload = { busy: boolean; url?: string; message?: string };

// Only real states exist:
type Upload =
  | { kind: "idle" }
  | { kind: "sending"; sentBytes: number }
  | { kind: "done"; url: string }
  | { kind: "failed"; message: string };
```

Use one tag name across the codebase.

## Branded types and honest guards

```ts
type OrderId = string & { readonly __brand: "OrderId" };

const isOrderId = (s: string): s is OrderId => /^ord_[a-z0-9]{12}$/.test(s);

export function parseOrderId(s: string): OrderId {
  if (!isOrderId(s)) throw new Error(`bad order id: ${s}`);
  return s;
}
```

Follow the brand shape the repo already uses.

## Build legal values

```ts
type NonEmpty<T> = [T, ...T[]];
const first = <T>(xs: NonEmpty<T>): T => xs[0];

type Span = { start: number; length: number }; // store start plus length, not start and end that can cross
```

If callers can already pass an empty array and you handle it, keep `T[]`.

## `unknown`, schemas, and edges

```ts
const User = z.object({ id: z.string(), age: z.number().int() });
type User = z.infer<typeof User>;

export function readUser(raw: unknown): User {
  return User.parse(raw); // the only place raw data becomes a User
}
```

`Record<string, unknown>` must not travel past this function.

## `satisfies`

```ts
const routes = { home: "/", cart: "/cart" } satisfies Record<string, `/${string}`>;
// routes.home keeps the literal type "/"
```

## Exhaustive switch

```ts
function label(u: Upload): string {
  switch (u.kind) {
    case "idle": return "waiting";
    case "sending": return `${u.sentBytes} bytes`;
    case "done": return u.url;
    case "failed": return u.message;
    default: {
      const _never: never = u;
      return _never;
    }
  }
}
```

## Derived types and options objects

```ts
type Row = Awaited<ReturnType<typeof loadRow>>;
type Patch = Partial<Pick<Row, "name" | "email">>;

function schedule(opts: { at: Date; retries: number; quiet: boolean }) {}
```
