import wx


class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Demo Panel vs Sizer", size=(600, 400))

        # Panel chính (màu xám)
        main_panel = wx.Panel(self)
        main_panel.SetBackgroundColour("#DDDDDD")

        # Main sizer chia VERTICAL (trên + dưới)
        main_sizer = wx.BoxSizer(wx.VERTICAL)

        # ---------- Toolbar Panel (màu vàng) ----------
        toolbar_panel = wx.Panel(main_panel)
        toolbar_panel.SetBackgroundColour("#FFD966")

        toolbar_sizer = wx.BoxSizer(wx.HORIZONTAL)
        btn1 = wx.Button(toolbar_panel, label="Button 1")
        btn2 = wx.Button(toolbar_panel, label="Button 2")
        toolbar_sizer.Add(btn1, 0, wx.ALL, 5)
        toolbar_sizer.Add(btn2, 0, wx.ALL, 5)
        toolbar_panel.SetSizer(toolbar_sizer)

        main_sizer.Add(toolbar_panel, 0, wx.EXPAND | wx.ALL, 5)

        # ---------- Body Panel (màu đỏ) ----------
        body_panel = wx.Panel(main_panel)
        body_panel.SetBackgroundColour("#FF7066")  # ✅ Đặt màu cho Panel, không phải Sizer
        body_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Sidebar (màu xanh lá)
        sidebar_panel = wx.Panel(body_panel, size=(150, -1))
        sidebar_panel.SetBackgroundColour("#21CE38")
        body_sizer.Add(sidebar_panel, 0, wx.EXPAND | wx.ALL, 5)

        # Content (màu xanh dương)
        content_panel = wx.Panel(body_panel)
        content_panel.SetBackgroundColour("#29C2FF")
        body_sizer.Add(content_panel, 1, wx.EXPAND | wx.ALL, 5)

        body_panel.SetSizer(body_sizer)
        main_sizer.Add(body_panel, 1, wx.EXPAND)

        main_panel.SetSizer(main_sizer)


if __name__ == "__main__":
    app = wx.App(False)
    frame = MainFrame()
    frame.Show()
    app.MainLoop()
