import {LitElement, css } from 'lit';
import {html, TemplateResult} from "lit-html";
import {customElement} from 'lit/decorators.js';
import { counterMachine } from "../../model/xstate-counter/xstate-counter";
import { interpret } from "xstate";

@customElement('my-counter')
class MyCounter extends LitElement {

  static override styles = css`
  :host {
    display: block;
    border: solid 1px gray;
    padding: 16px;
    max-width: 800px;
  }
`;

  private counterMachine = interpret(counterMachine);

  override render(): TemplateResult {
    return html`
      <button @click="${() => this.counterMachine.send("DEC")}">-</button>
      <span>${this.counterMachine.state.context.count}</span>
      <button @click="${() => this.counterMachine.send('INC')}">+</button>
    `;
  }

  override connectedCallback(): void {
    this.counterMachine.start();

    this.counterMachine.onTransition((state: any) => {
        if (state.changed){ 
          this.requestUpdate();
        }
    });

    super.connectedCallback();
}
}

export{ MyCounter }