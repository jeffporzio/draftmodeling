import { createMachine, assign } from 'xstate';

type CounterEvent =
  { type: 'INC' }
  | { type: 'DEC' };

interface counterContext {
  count: number;
}

export const counterMachine = createMachine<counterContext, CounterEvent>({
  initial: 'active',
  context: { count: 0 },
  states: {
    active: {
      on: {
        INC: {
          actions: assign({
            count: ctx => {
              return ctx.count + 1
            }
          })
        },
        DEC: {
          actions: assign({
            count: ctx => {
              return ctx.count - 1
            }
          })
        }
      }
    }
  }
});