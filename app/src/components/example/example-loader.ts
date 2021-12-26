import {LitElement, html, TemplateResult } from 'lit';
import {customElement} from 'lit/decorators.js';

@customElement("example-element-loader")
class exampleElementLoader extends LitElement {
    override render(): TemplateResult {
        return html`<example-element></example-element>`;
    }
}

export { exampleElementLoader } 
