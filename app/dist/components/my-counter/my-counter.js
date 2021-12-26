var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
import { LitElement, css } from 'lit';
import { html } from "lit-html";
import { customElement } from 'lit/decorators.js';
import { counterMachine } from "../../model/xstate-counter/xstate-counter";
import { interpret } from "xstate";
let MyCounter = class MyCounter extends LitElement {
    constructor() {
        super(...arguments);
        this.counterMachine = interpret(counterMachine);
    }
    render() {
        return html `
      <button @click="${() => this.counterMachine.send("DEC")}">-</button>
      <span>${this.counterMachine.state.context.count}</span>
      <button @click="${() => this.counterMachine.send('INC')}">+</button>
    `;
    }
    connectedCallback() {
        this.counterMachine.start();
        this.counterMachine.onTransition((state) => {
            if (state.changed) {
                this.requestUpdate();
            }
        });
        super.connectedCallback();
    }
};
MyCounter.styles = css `
  :host {
    display: block;
    border: solid 1px gray;
    padding: 16px;
    max-width: 800px;
  }
`;
MyCounter = __decorate([
    customElement('my-counter')
], MyCounter);
export { MyCounter };
//# sourceMappingURL=my-counter.js.map