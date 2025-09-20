import wx
import wx.grid as gridlib


class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="POSync - Cửa sổ chính", size=(800, 520))

        # Tạo menu
        self._create_menu_bar()

        # Tạo status bar
        self.CreateStatusBar()
        self.SetStatusText("Sẵn sàng")

        # Tạo panel chính và layout
        panel = wx.Panel(self)
        main_sizer = wx.BoxSizer(wx.VERTICAL)

        # Top: một Toolbar đơn giản (dùng sizer để giả toolbar)
        toolbar_sizer = wx.BoxSizer(wx.HORIZONTAL)
        btn_load = wx.Button(panel, label="Load")
        btn_import = wx.Button(panel, label="Import")
        btn_export = wx.Button(panel, label="Export")
        toolbar_sizer.Add(btn_load, 0, wx.ALL, 4)
        toolbar_sizer.Add(btn_import, 0, wx.ALL, 4)
        toolbar_sizer.Add(btn_export, 0, wx.ALL, 4)
        main_sizer.Add(toolbar_sizer, 0, wx.EXPAND | wx.LEFT | wx.RIGHT)

        # Bottom: log / output box
        self.log_load_label = wx.StaticText(panel, label="Load Log")
        self.log_import_label = wx.StaticText(panel, label="Import Log")
        self.log_export_label = wx.StaticText(panel, label="Export Log")
        self.log_load = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY, size=(-1, 80))
        self.log_import = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY, size=(-1, 80))
        self.log_export = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY, size=(-1, 80))

        # Sizer riêng cho vùng log
        self.log_sizer = wx.BoxSizer(wx.VERTICAL)
        self.log_sizer.Add(self.log_load_label, 0, wx.LEFT | wx.TOP, 12)
        self.log_sizer.Add(self.log_load, 1, wx.EXPAND | wx.ALL, 12)
        self.log_sizer.Add(self.log_import_label, 0, wx.LEFT | wx.TOP, 12)
        self.log_sizer.Add(self.log_import, 1, wx.EXPAND | wx.ALL, 12)
        self.log_sizer.Add(self.log_export_label, 0, wx.LEFT | wx.TOP, 12)
        self.log_sizer.Add(self.log_export, 1, wx.EXPAND | wx.ALL, 12)
        main_sizer.Add(self.log_sizer, 0, wx.EXPAND)

        # Ẩn log_import và log_export ban đầu, chỉ hiện log_load
        self.log_load.Hide()
        self.log_import.Hide()
        self.log_export.Hide()

        panel.SetSizer(main_sizer)
        self.panel = panel  # Lưu lại panel để dùng cho Layout()

        # Gắn sự kiện
        self.Bind(wx.EVT_BUTTON, self.on_load, btn_load)
        self.Bind(wx.EVT_BUTTON, self.on_import, btn_import)
        self.Bind(wx.EVT_BUTTON, self.on_export, btn_export)

        self.Show()

    def _create_menu_bar(self):
        menu_bar = wx.MenuBar()

        file_menu = wx.Menu()
        mi_exit = file_menu.Append(wx.ID_EXIT, 'E&xit\tCtrl-Q', 'Thoát chương trình')
        self.Bind(wx.EVT_MENU, self.on_exit, mi_exit)

        help_menu = wx.Menu()
        mi_about = help_menu.Append(wx.ID_ABOUT, '&About\tF1', 'Thông tin')
        self.Bind(wx.EVT_MENU, self.on_about, mi_about)

        menu_bar.Append(file_menu, '&File')
        menu_bar.Append(help_menu, '&Help')
        self.SetMenuBar(menu_bar)

    # Logic functions
    def on_load(self, event):
        self.log_load.Show()
        self.log_import.Hide()
        self.log_export.Hide()
        self.panel.Layout()
        self.log_load.AppendText('New clicked\n')
        self.SetStatusText('Load action')

    def on_import(self, event):
        self.log_load.Hide()
        self.log_import.Show()
        self.log_export.Hide()
        self.panel.Layout()
        dlg = wx.FileDialog(self, "Open file", wildcard="All files (*.*)|*.*",
                            style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            self.log_import.AppendText(f'Opened: {path}\n')
            self.SetStatusText(f'Opened: {path}')
        dlg.Destroy()

    def on_export(self, event):
        self.log_load.Hide()
        self.log_import.Hide()
        self.log_export.Show()
        self.panel.Layout()
        dlg = wx.FileDialog(self, "Save file", wildcard="All files (*.*)|*.*",
                            style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            self.log_export.AppendText(f'Saved: {path}\n')
            self.SetStatusText(f'Saved: {path}')
        dlg.Destroy()

    def on_about(self, event):
        wx.MessageBox('wxPython demo\nAuthor: ChatGPT', 'About', wx.OK | wx.ICON_INFORMATION)

    def on_exit(self, event):
        self.Close()


if __name__ == '__main__':
    app = wx.App(False)
    frame = MainFrame()
    app.MainLoop()
