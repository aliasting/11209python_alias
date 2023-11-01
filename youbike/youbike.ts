
import { Command } from "vscode";

export default class YoubikeCommand extends Command {
    constructor(context: ExtensionContext) {
        super(context);
    }

    public async execute(args: any): Promise<void> {
        const { location } = context.extensionUri;
        const query = args.query;

        const url = `https://youbike.tw/youbike/stationStatus?stationName=${query}`;
        const response = await fetch(url);
        const data = await response.json();

        console.log(data);
    }
}