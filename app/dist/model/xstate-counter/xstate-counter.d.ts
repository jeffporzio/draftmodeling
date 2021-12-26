declare type CounterEvent = {
    type: 'INC';
} | {
    type: 'DEC';
};
interface counterContext {
    count: number;
}
export declare const counterMachine: import("xstate").StateMachine<counterContext, any, CounterEvent, {
    value: any;
    context: counterContext;
}, import("xstate").ActionObject<counterContext, CounterEvent>>;
export {};
//# sourceMappingURL=xstate-counter.d.ts.map