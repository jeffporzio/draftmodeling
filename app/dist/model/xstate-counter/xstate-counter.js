import { createMachine, assign } from 'xstate';
export const counterMachine = createMachine({
    initial: 'active',
    context: { count: 0 },
    states: {
        active: {
            on: {
                INC: {
                    actions: assign({
                        count: ctx => {
                            return ctx.count + 1;
                        }
                    })
                },
                DEC: {
                    actions: assign({
                        count: ctx => {
                            return ctx.count - 1;
                        }
                    })
                }
            }
        }
    }
});
//# sourceMappingURL=xstate-counter.js.map