var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
import { LitElement, html } from 'lit';
import { customElement, property } from 'lit/decorators.js';
import { styles } from './example-styles';
let exampleElement = class exampleElement extends LitElement {
    constructor() {
        super();
        // Declare observed properties
        this.adjective = 'awesome';
    }
    // Define the element's template
    render() {
        return html `<p>your ${this.adjective} template here</p>`;
    }
};
exampleElement.styles = [styles];
__decorate([
    property()
], exampleElement.prototype, "adjective", void 0);
exampleElement = __decorate([
    customElement('example-element')
], exampleElement);
export { exampleElement };
//# sourceMappingURL=example-element.js.map