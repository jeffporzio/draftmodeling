import {LitElement} from 'lit';
import {html, TemplateResult} from 'lit-html';
import {customElement} from 'lit/decorators.js';

@customElement("example-element-loader")
class exampleElementLoader extends LitElement {

    count: number = 0;

    override render(): TemplateResult {
        return html`<my-counter></my-counter>`;
    }
}

export { exampleElementLoader } 
