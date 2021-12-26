var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
import { LitElement } from 'lit';
import { html } from 'lit-html';
import { customElement } from 'lit/decorators.js';
let exampleElementLoader = class exampleElementLoader extends LitElement {
    constructor() {
        super(...arguments);
        this.count = 0;
    }
    render() {
        return html `<my-counter></my-counter>`;
    }
};
exampleElementLoader = __decorate([
    customElement("example-element-loader")
], exampleElementLoader);
export { exampleElementLoader };
//# sourceMappingURL=my-counter-loader.js.map