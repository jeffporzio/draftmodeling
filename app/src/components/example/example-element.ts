import {LitElement, html, TemplateResult } from 'lit';
import {customElement, property} from 'lit/decorators.js';
import { styles } from './example-styles';

@customElement('example-element')
class exampleElement extends LitElement {

    static override styles = [styles];

    // Declare observed properties
    @property()
    adjective = 'awesome';

    constructor(){
        super();
    }

    // Define the element's template
    override render(): TemplateResult {
        return html`<p>your ${this.adjective} template here</p>`;
    }
}

export{ exampleElement }