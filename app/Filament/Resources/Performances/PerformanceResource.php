<?php

namespace App\Filament\Resources\Performances;

use App\Filament\Resources\Performances\Pages\CreatePerformance;
use App\Filament\Resources\Performances\Pages\EditPerformance;
use App\Filament\Resources\Performances\Pages\ListPerformances;
use App\Models\Performance;
use Filament\Forms;
use Filament\Schemas\Schema;
use Filament\Resources\Resource;
use Filament\Tables;
use Filament\Tables\Table;
use Filament\Forms\Components\Section;
use Filament\Tables\Columns\TextColumn;
use Filament\Tables\Actions\EditAction;

class PerformanceResource extends Resource
{
    protected static ?string $model = Performance::class;

    protected static string | \BackedEnum | null $navigationIcon = 'heroicon-o-chart-bar';

    public static function form(Schema $schema): Schema
    {
        return $schema
            ->components([
                Forms\Components\Grid::make(3)
                    ->schema([
                        Forms\Components\Section::make('Contexto do Jogo')
                            ->columnSpan(1)
                            ->schema([
                                Forms\Components\Select::make('game_id')
                                    ->relationship('game', 'map_name')
                                    ->label('Mapa/Set')
                                    ->required()
                                    ->searchable()
                                    ->preload(),
                                Forms\Components\Select::make('player_id')
                                    ->relationship('player', 'name')
                                    ->label('Jogador')
                                    ->required()
                                    ->searchable()
                                    ->preload(),
                                Forms\Components\TextInput::make('brawler_name')
                                    ->label('Brawler')
                                    ->required(),
                                Forms\Components\Toggle::make('is_win')
                                    ->label('Vitória?')
                                    ->onColor('success'),
                            ]),

                        Forms\Components\Section::make('Estatísticas de Combate')
                            ->columnSpan(2)
                            ->schema([
                                Forms\Components\Grid::make(2)->schema([
                                    Forms\Components\TextInput::make('kills')
                                        ->numeric()
                                        ->default(0)
                                        ->required(),
                                    Forms\Components\TextInput::make('deaths')
                                        ->numeric()
                                        ->default(0)
                                        ->required(),
                                    Forms\Components\TextInput::make('damage_dealt')
                                        ->numeric()
                                        ->label('DPS')
                                        ->default(0),
                                    Forms\Components\TextInput::make('damage_received')
                                        ->numeric()
                                        ->label('Damage Received')
                                        ->default(0),
                                    Forms\Components\TextInput::make('healing')
                                        ->numeric()
                                        ->label('Healing')
                                        ->default(0),
                                    Forms\Components\TextInput::make('damage_to_safe')
                                        ->numeric()
                                        ->label('Damage to Safe')
                                        ->default(0),
                                ]),
                                
                                Forms\Components\TextInput::make('rating_bser')
                                    ->numeric()
                                    ->label('Rating 1.0')
                                    ->helperText('Rating 1.0')
                                    ->required()
                                    ->extraInputAttributes(['style' => 'font-size: 1.5rem; font-weight: bold; color: #fbbf24;']),
                            ]),
                    ])
            ]);
    }

    public static function table(Table $table): Table
    {
        return $table
            ->columns([
                Tables\Columns\TextColumn::make('player.name')
                    ->label('Player')
                    ->sortable()
                    ->searchable(),
                Tables\Columns\TextColumn::make('brawler_name')
                    ->label('Brawler'),
                Tables\Columns\TextColumn::make('game.map_name')
                    ->label('Map'),
                Table\Columns\TextColumn::make('rating_bser')
                    ->label('Rating 1.0')
                    ->badge()
                    ->color(fn (string $state): string => match (true) {
                        $state >= 1.20 => 'success',
                        $state < 0.85 => 'danger',
                        default => 'warning',
                    })
                    ->sortable(),
                Tables\Columns\IconColumn::make('is_win')
                    ->boolean()
                    ->label('W'),
            ])
            ->defaultSort('created_at', 'desc');
    }

    public static function getRelations(): array
    {
        return [
            //
        ];
    }

    public static function getPages(): array
    {
        return [
            'index' => ListPerformances::route('/'),
            'create' => CreatePerformance::route('/create'),
            'edit' => EditPerformance::route('/{record}/edit'),
        ];
    }
}
